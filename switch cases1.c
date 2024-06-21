#include<stdio.h>
#include<math.h>
void main()
{
	int choice; //11 21 31 
	scanf("%d",&choice)
	switch(choice)
	case 11:
		printf("U have entered the breakfast menu items");
		printf("a.idly----35\n");
		printf("b.wada----45\n");
		printf("c.dosa----50\n");
		char item;
		scanf("%c",&char);
		printf("\nenter the quantity required");
		int unit;
		float total;
		scanf("%d",&quantity);
		switch(item)
		{
			case 'a':
				total=(unit*35*0.05)+(unit*35);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
			case 'b' :
				total=(unit*45*0.05)+(unit*45);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
			case 'c' :
			    total=(unit*50*0.05)+(unit*50);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
				
		}
	    break; 
	    case 21:
		printf("U have entered the lunch menu items");
		printf("a.full meals----120\n");
		printf("b.single meals----90\n");
		printf("c.fried rice----60\n");
		printf("d.jeera rice----100\n");
		char item;
		scanf("%c",&char);
		printf("\nenter the quantity required");
		int unit;
		float total;
		scanf("%d",&quantity);
		switch(item)
		{
			case 'a':
				total=(unit*120*0.05)+(unit*120);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
			case 'b' :
				total=(unit*90*0.05)+(unit*90);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
			case 'c' :
			    total=(unit*60*0.05)+(unit*60);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
			case d :
				total=(unit*100*0.05)+(unit*100);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
		} break;
		case 31:
			case 21:
		printf("U have entered the lunch menu items");
		printf("a.paratha----50\n");
		printf("b.butter chicken ----150\n");
		printf("c.romali roti----16\n");
		printf("d.schezwan fried rice----200\n");
		char item;
		scanf("%c",&char);
		printf("\n enter the quantity required");
		int unit;
		float total;
		scanf("%d",&quantity);
		switch(item)
		{
			case 'a':
				total=(unit*50*0.05)+(unit*50);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
			case 'b' :
				total=(unit*150*0.05)+(unit*150);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
			case 'c' :
			    total=(unit*16*0.05)+(unit*16);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
			case 'd' :
				total=(unit*200*0.05)+(unit*200);
				printf("ur bill  amount is %.2f",roundf(total));
				break;
		} break;
		
}