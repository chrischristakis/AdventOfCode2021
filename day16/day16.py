from functools import reduce


def hex_to_bin(hex):
    bits = len(hex) * 4
    # the [2:] is to remove the '0b' from the result
    return bin(int(hex, 16))[2:].zfill(bits)


def chunk(packet, length):
    chunk = packet[:length]
    packet[:] = packet[length:]
    return int("".join(chunk), 2)


def chunk_bin(packet, length):
    chunk = packet[:length]
    packet[:] = packet[length:]
    return "".join(chunk)


def part1_and_part2():
    with open("input") as file:
        version_sum = 0

        def get_version_and_type(packet):
            version = chunk(packet, 3)
            type = chunk(packet, 3)
            return version, type

        def decode(bin):
            version, type = get_version_and_type(bin)
            nonlocal version_sum
            version_sum += version

            match type:
                case 0: op = lambda lis: reduce((lambda x, y: x + y), lis)
                case 1: op = lambda lis: reduce((lambda x, y: x * y), lis)
                case 2: op = lambda lis: min(lis)
                case 3: op = lambda lis: max(lis)
                case 5: op = lambda lis: 1 if lis[0] > lis[1] else 0
                case 6: op = lambda lis: 1 if lis[0] < lis[1] else 0
                case 7: op = lambda lis: 1 if lis[0] == lis[1] else 0

            if type == 4:
                return decode_literal(bin)
            else:
                type_id = chunk(bin, 1)
                if type_id == 1:
                    return decode_num_operator(bin, op)
                else:
                    return decode_len_operator(bin, op)

        # For # of packets
        def decode_num_operator(packet, op):
            num_of_packets = chunk(packet, 11)
            literals = []
            for i in range(num_of_packets):
                literals.append(decode(packet))
            return op(literals)

        # For specified num of bits
        def decode_len_operator(packet, op):
            num_of_bits = chunk(packet, 15)
            og_len = len(packet)
            literals = []
            while og_len - len(packet) < num_of_bits:
                literals.append(decode(packet))
            return op(literals)

        def decode_literal(packet):
            result = ""
            bits_parsed = 6  # 6 Since we already parsed version and type, which are part oof this packet.
            while chunk(packet, 1) == 1:
                result += chunk_bin(packet, 4)
                bits_parsed += 5
            result += chunk_bin(packet, 4)
            return int(result, 2)

        # part 1
        bin = list(hex_to_bin(file.readline().rstrip()))
        sln2 = decode(bin)
        sln1 = version_sum

    return sln1, sln2


if __name__ == "__main__":
    print("Part 1 and 2 sln:", part1_and_part2())
