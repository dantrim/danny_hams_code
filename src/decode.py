from hamming_utils import decode

from argparse import ArgumentParser


def main():

    parser = ArgumentParser(
        description="Encode a data value of a specified number of bits"
    )
    parser.add_argument(
        "input", help="The input data to decode as a hex string (e.g. 0x4235)"
    )
    parser.add_argument(
        "encodedsize", help="The size in number of bits of the input, encoded message"
    )
    parser.add_argument(
        "outputsize", help="The size in number of bits of the pre-encoded message"
    )
    args = parser.parse_args()

    input_data = int(args.input, 16)
    input_binary_string = f"{bin(input_data)[2:]:0>{args.encodedsize}}"
    n_bits_in_encoded_message = int(args.outputsize)

    decoded_binary_string = decode(input_binary_string, n_bits_in_encoded_message)
    decoded_value = int(decoded_binary_string, 2)
    print(f"Input value         : 0x{args.input}")
    print(
        f"Input value (bin)   : 0b{input_binary_string}, size = {len(input_binary_string)} bits"
    )
    print(f"Decoded value       : 0x{hex(decoded_value)[2:]}")
    print(
        f"Decoded value (bin) : 0b{decoded_binary_string}, size = {len(decoded_binary_string)} bits"
    )


if __name__ == "__main__":
    main()
