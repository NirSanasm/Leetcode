class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        stack = []

        for asteroid in asteroids:

            if not stack:
                stack.append(asteroid)
            else:
                if stack[-1] > 0 and asteroid < 0:
                    if abs(asteroid) < stack[-1]:
                        continue
                    elif abs(asteroid) == stack[-1]:
                        stack.pop()
                    else:
                        stack.pop()
                        to_add = True
                        while stack:
                            if stack[-1] < 0:
                                break
                            elif stack[-1] > abs(asteroid):
                                to_add = False
                                break
                            
                            elif stack[-1] == abs(asteroid):
                                to_add = False
                                stack.pop()
                                break

                            else:
                                
                                stack.pop()
                        
                        if to_add:
                            stack.append(asteroid)
                else:
                    stack.append(asteroid)
                                

                                



        return stack
        