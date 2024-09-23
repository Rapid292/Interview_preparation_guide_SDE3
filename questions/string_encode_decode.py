class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f"{len(word)}" + "#" + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        end = 0
        decoded_list = []
        while end < len(s):
            word_count_index = end
            while s[word_count_index+1] != "#":
                word_count_index += 1
            word_count = int(s[end:word_count_index+1])
            start = word_count_index + 2
            end = start + word_count
            word = s[start:end]
            decoded_list.append(word)

            word_count_index = end

        return decoded_list