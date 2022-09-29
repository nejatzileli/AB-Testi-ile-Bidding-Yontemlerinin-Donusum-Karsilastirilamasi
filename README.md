# AB-Testi ile Bidding Yontemlerinin Donusumlerinin Karsilastirilmasi


Story: Lately, Facebook (Meta) launched a bidding system called 'MAXIMUM BIDDING' as an alternative
to the 'AVERAGE BIDDING' which is already on use. 'BOMBABOMBA.COM' which is our customer would like to test this 'MAXIMUM BIDDING SYSTEM'. They would like to know if the new bidding system really increases the customer conversion rate or not. To understand that, they are going to use A/B testing.

What Bombabombda.com wants?

A/B testing process is continueing and Bombabomba.com wants you to analyze A/B testing results. The success factor of this A/B test is 'PURCHASE'. Therefore, we need to focus on the PURCHASE metric.

DATASET: Advertisement Impression Count, Click-through rate for ads, purchase after click, earning after purchases. Important: There are two datasets with the same feature names. One for Maximum bidding, the other for average bidding.

Actions: 

1. Preprocessing and analyzing for both control and test group data. Concatinating these data.
2. Define the A/B testing hyphotesis for normality andvarience homogenity.
H0: Normality assumptions are true.
H1: Normality assumptions are not true
H0: Variences are homogenous.
H1: Variences are not homogenous.
p<0.05 H0 is rejected.
p>0.05 H0 failed to reject.
3. Since both assumptions are true, we use T-TEST (PARAMETRIC).
H0: M1 = M2 (There is no difference between purchase means of control group and the test group.
H1: M1 != M2 (Statistically, there is a difference betweeen purchase means of the control and test group.



