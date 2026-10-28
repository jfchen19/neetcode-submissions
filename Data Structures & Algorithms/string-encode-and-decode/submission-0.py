class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for s in strs:
            encode_string = encode_string + f"{len(s)}#{s}"
        return encode_string

        # return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        decoded_strs, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded_strs.append(word)
            i = j + 1 + length
        return decoded_strs
