#!/bin/env python

#
# Hamming(7,4) generator using the matrix form,
# taken from Wikipedia: https://en.wikipedia.org/wiki/Hamming(7,4)#Hamming_matrices
#
# author: Daniel Joseph Antrim
# date: December 2020
#

import sys
from argparse import ArgumentParser

import numpy as np


def encode(nibble):

    if len(nibble) != 4:
        print("Input nibble is not length 4!")
        sys.exit(1)

    # wiki matrix G
    code_generator = np.array(
        [
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )
    data = np.array(nibble)
    return list(np.mod(np.matmul(code_generator, data), 2))


def decode(input_data):

    if len(input_data) != 7:
        print("Input data for decoding is not length 7!")
        sys.exit(1)

    # wiki matrix H
    parity_check_matrix = np.array(
        [[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]]
    )
    data = np.array(input_data)

    # wiki vector z
    syndrom_vector = np.mod(np.matmul(parity_check_matrix, data), 2)

    if syndrom_vector.any():
        corrupted_bit = "".join(map(str, syndrom_vector))
        # count from zero
        corrupted_bit = int(corrupted_bit, 2) - 1
        corrupted_bit = 7 - corrupted_bit
        data[corrupted_bit] = not data[corrupted_bit]

    # wiki matrix R
    decode_matrix = np.array(
        [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
        ]
    )
    return np.mod(np.matmul(decode_matrix, data), 2)


def to_binary_string(input_list):

    """
    Assumes element at index 0 is the LSB.
    """
    return "".join(map(str, reversed(input_list)))


def nibbles(input_data_list):
    for i in range(0, len(input_data_list), 4):
        yield input_data_list[i : i + 4]


def main():
    parser = ArgumentParser(description="Testing Hamming(7,4)")
    parser.add_argument("input", help="Input hexadecimal string", type=str)
    parser.add_argument("length", help="Number of nibbles in input", type=int)
    args = parser.parse_args()

    input_data = int(args.input, 16)

    n_bits_expected = args.length * 4
    b_input_data = bin(input_data)[2:]
    input_binary_string = f"{b_input_data:0>{n_bits_expected}}"
    print(
        f"Input (len={len(input_binary_string):02d})     : {input_binary_string} ({int(input_binary_string,2)})"
    )
    input_binary = list(map(int, reversed(list(input_binary_string))))

    input_nibbles = [x for x in nibbles(input_binary)]
    encoded_nibbles = [encode(x) for x in input_nibbles]
    encoded_binary_string = "".join(map(to_binary_string, reversed(encoded_nibbles)))
    print(
        f"Encoded (len={len(encoded_binary_string):02d})   : {encoded_binary_string} ({int(encoded_binary_string,2)})"
    )

    decoded = [to_binary_string(list(decode(x))) for x in encoded_nibbles]
    decoded_binary_string = "".join(reversed(decoded))
    print(
        f"Decoded (len={len(decoded_binary_string):02d})   : {decoded_binary_string} ({int(decoded_binary_string,2)})"
    )

    output_matches_input = int(input_binary_string, 2) == int(decoded_binary_string, 2)
    print(f"==> Decoding success? {output_matches_input}")


if __name__ == "__main__":
    main()
