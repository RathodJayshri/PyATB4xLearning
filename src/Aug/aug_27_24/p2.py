# functions scope
public_washroom = "PB"
def home():
    private_washroom = "PT"
    print(public_washroom)
    print(private_washroom)

def strange():
    print(public_washroom)

print(public_washroom)
# print(private_washroom) we cant access outside

