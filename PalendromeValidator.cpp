#include <iostream>
#include <vector>

int main(){
    std::string word;
    std::cout << "\n";
    std::cout << "Please enter a word and I will tell you if it is a palindrome \n";
    std::cin >> word;
    std::vector<char> arr(word.begin(), word.end());
    int i = 0;
    int j = word.length() - 1;;
    bool isPalindrome = true;
    while(i < j){
       
        if(arr[i] != arr[j]){
            isPalindrome = false;
            std::cout << word << " is not a palindrome";
            break;
        }else{
            isPalindrome = true;
            std::cout << word << " is a palindrome";
            break;
        }
        i++;
        j--;
    }
}

