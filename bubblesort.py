class BubbleSort:
    def sort(self, input_str):
        nums = [int(char) for char in input_str]
        is_sorted = False
        print(nums)
        l_nums = len(nums)
        f_idx = 0
        fixes = 0

        while not is_sorted:
            s_idx = f_idx + 1
            first = nums[f_idx]
            second = nums[s_idx]
            if first > second:
                fixes += 1
                nums[f_idx] = second
                nums[s_idx] = first
                print(nums)

            f_idx = f_idx + 1
            if f_idx == l_nums - 1:
                if fixes == 0:
                    is_sorted = True
                else:
                    f_idx = 0
                    fixes = 0
            print("", end=".")


if __name__ == "__main__":
    BubbleSort().sort("653187246531872653187265318726531872653187265318726531872")
