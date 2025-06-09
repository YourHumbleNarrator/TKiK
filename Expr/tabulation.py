class AddTabulation:

    def tabulation(self, generated_c):

        tab_counter = 0
        generated_c2 = ""

        for line in generated_c.splitlines():

            if '{' in line:
                line = ('\t' * tab_counter) + line
                generated_c2 = generated_c2 + line + '\n'
                tab_counter = tab_counter + 1
            elif '}' in line:
                tab_counter = tab_counter - 1
                line = ('\t' * tab_counter) + line
                generated_c2 = generated_c2 + line + '\n'
            else:
                line = ('\t' * tab_counter) + line
                generated_c2 = generated_c2 + line + '\n'

        return generated_c2
