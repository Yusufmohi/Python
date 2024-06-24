class goa:
    name=""
    movie="rrr"
    def party(self):
        print("Lets Party")
    def beach(self):
        print("Enjoying the beach")

yusuf=goa()
mohi=goa()

yusuf.name="Yusuf"
mohi.name="Mohi"
yusuf.movie="Yes"
mohi.movie="No"

print(yusuf.name)
print("Movie:",yusuf.movie)
yusuf.party()
print(mohi.name)
print("Movie:",mohi.movie)
mohi.beach()
