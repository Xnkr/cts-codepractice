#include<iostream>

using namespace std;

int count = 0;

void generateNumSequence(int num){
	count++;
	if(num!=1){
		if(num%2==0){
			generateNumSequence(num/2);
		}
		else{
			generateNumSequence((3*num)+1);
		}		
	}
	else{
		cout<<count;
	}
}

int main(){
	int num = 1;
	cin>>num;
	if(num<=0){
		cout<<"Enter a number which is greater than zero";
	}
	else if(num > 100){
		cout<<"Length should not exceed more than 100";
	}
	else{
		generateNumSequence(num);
	}
	return 0;
}