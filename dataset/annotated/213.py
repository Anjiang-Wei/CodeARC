from typing import List, Union

def calculate_bits_battle_result(nums: List[int]) -> Union[str, None]:
    def bits_battle(nums: List[int]) -> str:
        binary = '{:b}'.format
        evens = odds = 0
        for num in nums:
            if num % 2:
                odds += binary(num).count('1')
            else:
                evens += binary(num).count('0')
        if odds == evens:
            return 'tie'
        return '{} win'.format('odds' if odds > evens else 'evens')
    
    return bits_battle(nums)

