class Solution {
    public boolean isValid(String s) {

        // Create a stack that is populated by an opening bracket/parenthesis and depopulated once the corresponding closer to said opening bracet/parenthesis is found directly afterwards. 
        Stack<Character> char_stack = new Stack<>();

        // Turn the string into a character array in order to safely assess the input string character by character.
        char[] ch = s.toCharArray();

        // A for loop is created so that each character in the 'string' (now character array) can be analysed on a case-by-case basis. 
        for (int i = 0; i < ch.length; i++) {
          
            // A switch case is implemented so that certain actions occur when certain characters appear.
            switch(ch[i]){
                // Whenever an opening bracket/parenthesis is being assessed it is added to the character stack.
                // No line breaks = all cases (w/o breaks) execute the same code.
                case '(':
                case '{':
                case '[':
                    char_stack.push(ch[i]);
                    break;
                
                // When a closing bracket is found, its opening match is searched for in the character array ahead of the closing bracket's/parenthesis' analysis.
                // If found, both characters are removed from the character array.
                case ')':
                    if (char_stack.isEmpty() || char_stack.pop() != '(') { return false; }
                    break;
                case '}':
                    if (char_stack.isEmpty() || char_stack.pop() != '{') { return false; }
                    break;
                case ']':
                    if (char_stack.isEmpty() || char_stack.pop() != '[') { return false; }
                    break;
            }
        }
      
      // If the character stack is empty following analysis of the entire 'string', then the input string would have been valid.
      if (char_stack.isEmpty()) { return true; }
      else { return false; }
    }
}
