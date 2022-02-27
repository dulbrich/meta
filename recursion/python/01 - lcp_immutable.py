class Solution:
    def letterCasePermutation(self, input_str: str) -> List[str]:
        solutions = []
        len_input = len(input_str)

        def fill_blanks(idx_subproblem, slate):
            # Base case
            if idx_subproblem == len_input:
                solutions.append(slate)
                return # Going back up

            # Recursive case
            if input_str[idx_subproblem].isdigit():
                fill_blanks(idx_subproblem + 1, slate + input_str[idx_subproblem])
            else:
                fill_blanks(idx_subproblem + 1, slate + input_str[idx_subproblem].lower())
                fill_blanks(idx_subproblem + 1, slate + input_str[idx_subproblem].upper())

s
        fill_blanks(0, "")

        return solutions