class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    ### 문제풀이 1: 정렬하여 딕셔너리에 추가
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())
        