class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key = lambda car: car[0], reverse=True)

        stack = [cars[0]]
        num_fleets = 1

        for i in range(1, len(cars)):
            prev_fleet = stack[-1]

            curr_time_to_dest = (target - cars[i][0]) / cars[i][1]
            prev_fleet_time_to_dest = (target - prev_fleet[0]) / prev_fleet[1]

            if curr_time_to_dest > prev_fleet_time_to_dest:
                num_fleets += 1
                stack.append(cars[i])
        
        return num_fleets






        

        