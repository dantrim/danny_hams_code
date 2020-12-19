from hamming_utils import encode

from argparse import ArgumentParser


def main():

    parser = ArgumentParser(
        description="Encode a data value of a specified number of bits"
    )
    parser.add_argument(
        "input", help="The input data to encode as a hex string (e.g. 0x4235)"
    )
    parser.add_argument("size", help="The size in number of bits of the data to encode")
    args = parser.parse_args()

    input_data = int(args.input, 16)
    input_binary_string = f"{bin(input_data)[2:]:0>{args.size}}"
    n_bits = int(args.size)

    encoded_binary_string = encode(input_data, n_bits)
    encoded_value = int(encoded_binary_string, 2)
    print(f"Input value         : 0x{args.input}, size = {args.size} bits")
    print(f"Input value (bin)   : 0b{input_binary_string}")
    print(f"Encoded value       : 0x{hex(encoded_value)[2:]}")
    print(
        f"Encoded value (bin) : 0b{encoded_binary_string}, size = {len(encoded_binary_string)} bits"
    )


if __name__ == "__main__":
    main()
