class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        forecast = []

        for i,t in enumerate(temperatures):

            next_day_warmer = 0

            for k in range(i+1,len(temperatures)):

                if temperatures[i] < temperatures[k]:
                    next_day_warmer = k-i
                    break
            
            forecast.append(next_day_warmer)
        
        return forecast