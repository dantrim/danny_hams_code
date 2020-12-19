# danny_hams_code
Some utilities for encoding and decoding messages using single-error correcting Hamming codes.

The encoding and decoding algorithms are derived from [tutorialspoint](https://www.tutorialspoint.com/error-correcting-codes-hamming-codes)
and the [Hamming Codes wikipedia entry](https://en.wikipedia.org/wiki/Hamming_code).

## Encode A Message

In order to encode a chunk of data of a specific number of bits, `n`, there is the `encode` utilty:
```shell
$ python src/encode.py -h
usage: encode.py [-h] input size

Encode a data value of a specified number of bits

positional arguments:
  input       The input data to encode as a hex string (e.g. 0x4235)
  size        The size in number of bits of the data to encode

optional arguments:
  -h, --help  show this help message and exit
  ```
  
For example, to encode a 16-bit message `0x4235`, one does:
```shell
$ python src/encode.py 4235 16
Input value         : 0x4235, size = 16 bits
Input value (bin)   : 0b0100001000110101
Encoded value       : 0x8a3ac
Encoded value (bin) : 0b010001010001110101100, size = 21 bits
```

## Decode A Message

In order to decode an `n`-bit message encoded in an `m`-bit chunk of data, there is the `decode` utility:
```shell
usage: decode.py [-h] input encodedsize outputsize

Encode a data value of a specified number of bits

positional arguments:
  input        The input data to decode as a hex string (e.g. 0x4235)
  encodedsize  The size in number of bits of the input, encoded message
  outputsize   The size in number of bits of the pre-encoded message

optional arguments:
  -h, --help   show this help message and exit
```

For example, to decode a 16-bit chunk of data contained in 21-bit message:
```shell
$ python src/decode.py 8a3ac 21 16
Input value         : 0x8a3ac
Input value (bin)   : 0b010001010001110101100, size = 21 bits
Decoded value       : 0x4235
Decoded value (bin) : 0b0100001000110101, size = 16 bits
```

## Single Bit Error Corrections

The implementation of the Hamming codes is such that it can detect and correct single-bit errors.
For example, in the [section above](#encode-a-message) we encoded the 16-bit value `0x4235`
into the 21-bit message `0x8a3ac` (`0b010001010001110101100`).

If a single bit were to be corrupted (flipped) in that 21-bit message, then the the
decoding algorithm will detect and correct it. For example, if we flip the bit
at position 4 (from the right) we get the 21-bit message `0x8a3a4` (`0b010001010001110100100`).
If we decode this single-bit corrupted message we get:
```shell
$ python src/decode.py 8a3a4 21 16
Input value         : 0x8a3a4
Input value (bin)   : 0b010001010001110100100, size = 21 bits
Decoded value       : 0x4235
Decoded value (bin) : 0b0100001000110101, size = 16 bits
```
Which gives us back the pre-encoded (and pre-corrupted), expected value of `0x4235`!
