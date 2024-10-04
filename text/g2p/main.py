from enum import Enum
from .phoneme_vocab import vocab
import os
from typing import List
import string, re


class VIETNAMESE_TONE(Enum):
    VIETNAMESE_TONE_NO_TONE = 0	 #z = bằng + cao*/
    VIETNAMESE_TONE_HUYEN = 1		#f = bằng + thấp*/
    VIETNAMESE_TONE_NGA = 2		#x = trắc + gẫy + cao*/
    VIETNAMESE_TONE_HOI = 3		#r = trắc + gẫy + thấp*/
    VIETNAMESE_TONE_SAC = 4		#s = trắc + không gẫy + cao*/
    VIETNAMESE_TONE_NANG = 5		#j = trắc + không gẫy + thấp*/

class VietnameseSyllable:
    def __init__(self):
        syllable = ''
        start = ''
        center = ''
        end = ''
        hnphonemes = ''
        vnphonemes = ''



class G2p_vi:

    def __init__(self):
        whereami = os.path.dirname(os.path.realpath(__file__))
        phones_file_path = os.path.join(whereami, 'phone_list.txt')
        with open(phones_file_path) as f:
            ls = f.read().splitlines()
        if ls:
            self.phone_ls = ls

        self.grapheme2phoneme = dict()
        self._build_phoneme_map()

    @classmethod
    def get_phone_ls(cls):
        whereami = os.path.dirname(os.path.realpath(__file__))
        phones_file_path = os.path.join(whereami, 'phone_list.txt')
        with open(phones_file_path) as f:
            ls = f.read().splitlines()
        return ls

    def get_tone_char(self, wch: str) -> VIETNAMESE_TONE:

        # if (wcschr(L"ÀàẰằẦầÈèỀềÌìÒòỒồỜờÙùỪừỲỳ", wch))	return VIETNAMESE_TONE_HUYEN;
        # if (wcschr(L"ÁáẮắẤấÉéẾếÍíÓóỐốỚớÚúỨứÝý", wch))	return VIETNAMESE_TONE_SAC;
        # if (wcschr(L"ẢảẲẳẨẩẺẻỂểỈỉỎỏỔổỞởỦủỬửỶỷ", wch))	return VIETNAMESE_TONE_HOI;
        # if (wcschr(L"ÃãẴẵẪẫẼẽỄễĨĩÕõỖỗỠỡŨũỮữỸỹ", wch))	return VIETNAMESE_TONE_NGA;
        # if (wcschr(L"ẠạẶặẬậẸẹỆệỊịỌọỘộỢợỤụỰựỴỵ", wch))	return VIETNAMESE_TONE_NANG;

        if  wch ==  'à' or wch ==  'À' or wch ==  'ằ' or wch ==  'Ằ' or wch ==  'ầ' or wch ==  'Ầ' or wch ==  'è' or wch ==  'È' or wch ==  'ề' or wch ==  'Ề' or wch ==  'ì' or wch ==  'Ì' or wch ==  'ò' or wch ==  'Ò' or wch ==  'ồ' or wch ==  'Ồ' or wch ==  'ờ' or wch ==  'Ờ' or wch ==  'ù' or wch ==  'Ù' or wch ==  'ừ' or wch ==  'Ừ' or wch ==  'ỳ' or wch ==  'Ỳ':
            return VIETNAMESE_TONE.VIETNAMESE_TONE_HUYEN
        if  wch ==  'á' or wch ==  'Á' or wch ==  'ắ' or wch ==  'Ắ' or wch ==  'ấ' or wch ==  'Ấ' or wch ==  'é' or wch ==  'É' or wch ==  'ế' or wch ==  'Ế' or wch ==  'í' or wch ==  'Í' or wch ==  'ó' or wch ==  'Ó' or wch ==  'ố' or wch ==  'Ố' or wch ==  'ớ' or wch ==  'Ớ' or wch ==  'ú' or wch ==  'Ú' or wch ==  'ứ' or wch ==  'Ứ' or wch ==  'ý' or wch ==  'Ý':            
            return VIETNAMESE_TONE.VIETNAMESE_TONE_SAC
        if  wch ==  'ả' or wch ==  'Ả' or wch ==  'ẳ' or wch ==  'Ẳ' or wch ==  'ẩ' or wch ==  'Ẩ' or wch ==  'ẻ' or wch ==  'Ẻ' or wch ==  'ể' or wch ==  'Ể' or wch ==  'ỉ' or wch ==  'Ỉ' or wch == 'ỏ' or wch ==  'Ỏ' or wch ==  'ổ' or wch ==  'Ổ' or wch ==  'ở' or wch ==  'Ở' or wch ==  'ủ' or wch ==  'Ủ' or wch ==  'ử' or wch ==  'Ử' or wch ==  'ỷ' or wch ==  'Ỷ':            
            return VIETNAMESE_TONE.VIETNAMESE_TONE_HOI
        if  wch ==  'ã' or wch ==  'Ã' or wch ==  'ẵ' or wch ==  'Ẵ' or wch ==  'ẫ' or wch ==  'Ẫ' or wch ==  'ẽ' or wch ==  'Ẽ' or wch ==  'ễ' or wch ==  'Ễ' or wch ==  'ĩ' or wch ==  'Ĩ' or wch ==  'õ' or wch ==  'Õ' or wch ==  'ỗ' or wch ==  'Ỗ' or wch ==  'ỡ' or wch ==  'Ỡ' or wch ==  'ũ' or wch ==  'Ũ' or wch ==  'ữ' or wch ==  'Ữ' or wch ==  'ỹ' or wch ==  'Ỹ':            
            return VIETNAMESE_TONE.VIETNAMESE_TONE_NGA
        if  wch ==  'ạ' or wch ==  'Ạ' or wch ==  'ặ' or wch ==  'Ặ' or wch ==  'ậ' or wch ==  'Ậ' or wch ==  'ẹ' or wch ==  'Ẹ' or wch ==  'ệ' or wch ==  'Ệ' or wch ==  'ị' or wch ==  'Ị' or wch == 'ọ' or wch ==  'Ọ' or wch ==  'ộ' or wch ==  'Ộ' or wch ==  'ợ' or wch ==  'Ợ' or wch ==  'ụ' or wch ==  'Ụ' or wch ==  'ự' or wch ==  'Ự' or wch ==  'ỵ' or wch ==  'Ỵ':
            return VIETNAMESE_TONE.VIETNAMESE_TONE_NANG
        return VIETNAMESE_TONE.VIETNAMESE_TONE_NO_TONE

    def get_tone(self, word: str) -> VIETNAMESE_TONE:
        for char in word:
            temp_tone = self.get_tone_char(char)
            if temp_tone != VIETNAMESE_TONE.VIETNAMESE_TONE_NO_TONE: return temp_tone
        return VIETNAMESE_TONE.VIETNAMESE_TONE_NO_TONE


    def g2p_split(self, word, delimit = '/'):
        phoneme_ls_txt = self.g2p_word(word)
        return delimit.join(phoneme_ls_txt.split(' '))
 
    def g2p_word(self, word) -> str:
        if word in self.grapheme2phoneme:
            return self.grapheme2phoneme[word]
        else:
            if word not in [',', '.']:
                print("erro: ", word)
            return "<SILENT>"


    def preprocess(self, text: str)-> str:
        for pt in string.punctuation:
            text = text.replace(pt, ' ' + pt + ' ')
        text = re.sub('\s+', ' ', text)
        return text

    def g2p(self, text: str, foreign_dict: dict=None, get_boundary: bool=True) -> List[str]:
        text = self.preprocess(text)
        phoneme_text, boundaries = [], []
        for word in text.split(' '):
            if word:
                iphoneme = self.g2p_word(word)
                phoneme_text.extend(iphoneme.split())
                # phoneme_text.append(' ')
                boundaries.append(len(iphoneme.split()))
        if phoneme_text[-1] == ' ':
            phoneme_text = phoneme_text[:-1]
       
        # return phoneme_text
        if get_boundary is True:
            if phoneme_text[-1] == "<SILENT>": phoneme_text[-1] = "</S>"
            return phoneme_text, boundaries
        else:
            if phoneme_text[-1] not in ["<SILENT>", "</S>"]: phoneme_text.append("<SILENT>")

        return phoneme_text


    def _build_phoneme_map(self):
        for isyllable in vocab:
            currentSyllable = isyllable[0]
            currentTone = self.get_tone(currentSyllable)
            currentEnd = isyllable[3]
            if (currentTone == VIETNAMESE_TONE.VIETNAMESE_TONE_NO_TONE and (currentEnd == "c" or currentEnd == "ch" or currentEnd == "p" or currentEnd == "t")):
                currentTone = VIETNAMESE_TONE.VIETNAMESE_TONE_SAC
            phonemesString = isyllable[5]

            if currentTone != VIETNAMESE_TONE.VIETNAMESE_TONE_NO_TONE:
                newPhonemeString = ""
                subphonemelist = phonemesString.split()
                for isubphoneme in subphonemelist:
                    newPhonemeString += isubphoneme
                    if (isubphoneme == "a"
                        or isubphoneme == "aa"
                        or isubphoneme == "aw"
                        or isubphoneme == "e"
                        or isubphoneme == "ea"
                        or isubphoneme == "ee"
                        or isubphoneme == "i"
                        or isubphoneme == "ie"
                        or isubphoneme == "o"
                        or isubphoneme == "oa"
                        or isubphoneme == "oo"
                        or isubphoneme == "ooo"
                        or isubphoneme == "ow"
                        or isubphoneme == "u"
                        or isubphoneme == "uo"
                        or isubphoneme == "uw"
                        or isubphoneme == "wa"):
                    
                        newPhonemeString += str(currentTone.value)
                    newPhonemeString += " "
                phonemesString = newPhonemeString

            self.grapheme2phoneme[currentSyllable] = phonemesString
            if isyllable[4] != isyllable[5]:
                self.grapheme2phoneme["vir" + currentSyllable] = isyllable[5]

    def __call__(self, text: str, foreign_dict: dict=None, get_boundary: bool=True):
        text = text.lower()
        # text = re.sub(_whitespace_re, " ", text)

        return self.g2p(text, foreign_dict=foreign_dict, get_boundary=get_boundary)

# if __name__ == '__main__':
#     ob = G2p_vi()
#     print(list(ob.grapheme2phoneme.keys())[:5])
#     # print(ob.get_tone('ặ') == VIETNAMESE_TONE.VIETNAMESE_TONE_NANG)
#     # print(ob.get_tone('ặ'))
#     print(ob.phonemize_vi('không'))