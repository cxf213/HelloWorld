#include <iostream>
#include <stdio.h>
#include <ctype.h>

int main(){
	char * str=new char[5];
	std::cin>>str;
	
	for(int i=0;i<5;i++){
		if(islower(str[i])){
			str[i]=(str[i]-'a'+4)%26+'a';
		}
		else{
			str[i]=(str[i]-'A'+4)%26+'A';
		}
	}
	
	printf("%s\n",str);
	//for(char a:str){
	//	putchar(a);
	//}
}
