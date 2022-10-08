import argparse
import math
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)

args = parser.parse_args()

P = args.principal
n = args.periods
interest = args.interest
pay = args.payment
list_D = []

alist = []

for arg in vars(args):
    if getattr(args, arg) is not None:
        alist.append(getattr(args, arg))


if (args.type != "diff" and args.type != "annuity") or (len(sys.argv) < 5) or (interest is None):
    print("Incorrect parameters")
else:
    if args.type == "diff" and pay is not None:
        print("Incorrect parameters")
    elif args.type == "diff":
        if P < 0 or n < 0 or interest < 0:
            print("Incorrect parameters")
        else:
            for i in range(1, n+1):
                inter = interest/1200
                D = math.ceil((P/n) + (inter * (P - ((P * (i-1)) / n))))
                print("Month", i, ": payment is", D)
                list_D.append(D)
            print()
            print("Overpayment =", sum(list_D) - P)

    elif args.type == "annuity":
        if pay is not None and P is not None and interest is not None:
            if pay < 0 or P < 0 or interest < 0:
                print("Incorrect parameters")
            elif pay > 0 and P > 0 and interest > 0:
                inter = interest/1200
                periods = math.ceil(math.log((pay / (pay - (inter * P))), (1 + inter)))

                if periods < 12:
                    print("It will take", periods, "months to repay this loan!")
                elif periods == 12:
                    print("It will take 1 year to repay this loan!")
                elif periods % 12 == 0:
                    time = periods // 12
                    print("It will take", time, "years to repay this loan!")
                else:
                    years = periods // 12
                    left_months = periods % 12
                    print("It will take", years, "years and", left_months, "months to repay this loan!")
                    print("Overpayment =", (periods * pay) - P)


        elif pay is not None and n is not None and interest is not None:
            if pay < 0 and n < 0 and interest < 0:
                print("Incorrect parameters")
            else:
                inter = interest/1200
                principal = math.floor(pay / ((inter * math.pow((1 + inter), n)) / (math.pow((1 + inter), n) - 1)))
                print("Your loan principal =",principal,"!")
                print("Overpayment =", (pay * n) - principal)

        elif P is not None and n is not None and interest is not None:
            inter = interest/1200
            amount = math.ceil(P * ((inter * math.pow((1 + inter), n)) / (math.pow((1 + inter), n) - 1)))
            print("Your annuity payment =",amount,"!")
            print("Overpayment =", (amount * n) - P)


