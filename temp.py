# # # import math, sys, re, random
# # #
# # # inp = [(0,0,1),(0,1,1),(1,0,1),(1,1,1)]
# # # theOut = [0,1,1,0]                  # theoretical output
# # # alpha = .1
# # #
# # #
# # # # FUNCTIONS
# # #
# # # #1
# # # def extractNNSpecs():
# # #     args = sys.argv[1:]               # command line arguments
# # #     if len(args)<1 or re.compile("^\\d+$").search(args[-1]) is not None:
# # #         args += [sys.argv[0] + "..\\..\\XOR.txt"]   # append the ...
# # #     fileLoc = args[-1]                # training set location
# # #     aTraining = open(fileLoc, "r").read().splitlines()  # make a list of the training set
# # #     aInitial, aFinal = [], []         # We'll separate the input and output
# # #     for idx in range(len(aTraining)): # For each training set item
# # #         strIn, strOut = aTraining[idx].split(" => ")  # separate it into input and output
# # #         # print ("'{}' ==> '{}'".format(strIn, strOut))
# # #         aInitial.append([float(mynum) for mynum in re.split(  # make each input part numeric
# # #           "\\s+,?\\s*|\\s*,?\\s+", strIn.strip())] + [1.0])   # trailing element is bias
# # #         aFinal.append  ([float(mynum) for mynum in re.split(  # make each output part numeric
# # #           "\\s+,?\\s*|\\s*,?\\s+", strOut.strip())])
# # #     # Fix the number of nodes per each layer
# # #     aLayerCt = [len(aInitial[0])] + [int(n) for n in args[:-1]] + [len(aFinal[0])]
# # #     return aInitial, aFinal, aLayerCt
# # #
# # # #2
# # # def randomWeights(numIn,numLayer,numOut):
# # #     weights = set()
# # #     numWeights = (numIn*numLayer)+(numLayer*numOut)+numOut
# # #     for i in range(numWeights):
# # #         weights.add(random.random()*2-1)
# # #     return weights
# # #
# # # #3
# # # def dotProduct(vector1,vector2):
# # #     return sum(i[0]*i[1] for i in zip(vector1,vector2))
# # #
# # # #4
# # # def displayNN(errorlist, weights):
# # #     print('Total error:',sum(errorlist))
# # #     print('Individual errors:',errorlist)
# # #     print('Weights:',weights)
# # #     print()
# # #
# # # #5
# # # def forwardNodes(i,weights):
# # #     node1 = dotProduct(i, weights[:3])
# # #     node2 = dotProduct(i, weights[3:7])
# # #     return (node1,node2)
# # #
# # #
# # # #6
# # #
# # # #function
# # # def f(x):
# # #     return 1/(1+math.e**(-x))
# # #
# # # def deriv(x):
# # #     return f(x)*(1-f(x))
# # #
# # # def error(theOut,expOut,nnWeights):
# # #     return [.5 * (theOut[i] - expOut[i]*nnWeights[8])**2 for i in range(len(expOut))]
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # MAIN
# # # # X01-inp1
# # # # X00-inp2   0
# # # # X10-bias   0   0
# # #
# # # extractNNSpecs()
# # # weights = randomWeights(3,2,1)
# # # # weights in order of first half go to the top node
# # # nnWeights = [weights.pop(),weights.pop(),weights.pop(),weights.pop(),weights.pop(),weights.pop(),
# # #              weights.pop(),weights.pop(),weights.pop()]
# # #
# # #
# # #
# # # errorsum = 9999.0
# # # numIts = 0
# # # expOut = [9999.9,9999.9,9999.9,9999.9]
# # # while errorsum > .0005:
# # #     numIts+=1
# # #     for p in range(len(inp)):
# # #         #forwardpropogation
# # #         # errorlist = []
# # #         xvals = []
# # #         for k in range(3):xvals.append(inp[p][k])
# # #
# # #
# # #         # for j in range(len(nnWeights)):
# # #         # for i in inp:   # make 2nd layer
# # #         node1,node2 = forwardNodes(inp[p],nnWeights)
# # #         xvals.append(node1)
# # #         xvals.append(node2)
# # #         expVal = dotProduct((node1,node2),nnWeights[6:9])
# # #         xvals.append(expVal)
# # #         expOut[p] = expVal
# # #         # print('expOut',expOut)
# # #         errorlist = error(theOut,expOut,nnWeights)
# # #         errorsum = sum(errorlist)/4
# # #
# # #
# # #         # print(xvals)
# # #         # exit()
# # #
# # #         #backpropogation
# # #         gradient = [0]*len(nnWeights)
# # #
# # #         # x it came from and error it goes to
# # #         EVal = [0]*len(nnWeights)
# # #         EVal[8] = (theOut[p]-xvals[5]*nnWeights[8])*nnWeights[8] * xvals[5]*(1-xvals[5])
# # #         gradient[8] = EVal[8]*xvals[5]
# # #         EVal[7] = sum(nnWeights)*EVal[8] * xvals[3]*(1-xvals[3])
# # #         gradient[7] = EVal[7]*xvals[3]
# # #         EVal[6] = sum(nnWeights)*EVal[7] * xvals[4]*(1-xvals[4])
# # #         gradient[6] = EVal[6]*xvals[4]
# # #
# # #         for x in [*range(6)][::-1]:
# # #             EVal[x] = sum(nnWeights)*EVal[x+1] * xvals[x%3]*(1-xvals[x])
# # #             gradient[x] = EVal[x]*xvals[x%3]
# # #
# # #         # for x in range(len(nnWeights)):
# # #         #     gradient[x] = xvals[x]*
# # #
# # #
# # #
# # #         # gradient[8] = (expOut[-1]-theOut[-1])*deriv(nnWeights[-1]*expOut[-2])
# # #
# # #         # gradient = [nnWeights[y] for y in range(len(nnWeights))]
# # #         # gradient[8] =
# # #         # update =
# # #         for i in range(len(nnWeights)):
# # #             nnWeights[i] = nnWeights[i]-gradient[i]*alpha
# # #
# # #
# # #
# # #         # displayNN(errorlist,nnWeights)
# # #         print(errorsum)
# # # print(numIts)
# # # print(expOut)
# # # print(nnWeights)
# # #
# # # #backpropogation
# # # # lasterror = [theOut[i]-expOut[i] for i in range(len(theOut))]
# # # # error = [errorlist[i]*lasterror[i]*deriv(xvals[i]) for i in range(len(lasterror))]
# #
# # # import random
# # # print(random.random()*4 - 2)
# #
# # # file = open("temp.out", "w")
# # #
# # # file.write("hello")
# # # file.write("\nhello2")
# # # file.write("")
# # # file.write("hello3")
# #
# # import datetime
# # # print(datetime.datetime.now())
# # print('%.2f' % 5.0)
#
# import numpy as np
# import random
#
#
# syn0array = [[-16.902669173023693, -22.235163842056092, -0.06071293554734092, 0.35558279005889953], [0.027854023254821052, -2.0656004376186514, 15.984893633030001, -12.825323452246845], [-12.057181451121938, 14.8883953082205, -12.376911708685327, -9.106254231718786]]
# syn1array = [[-36.962690520509604], [35.84300753846032], [-36.714820693618826], [-37.56901017105353]]
# syn0 = np.array(syn0array)
# syn1 = np.array(syn1array)
#
#
# numtest = 100000
# def nonlin(x, deriv=False):
#     if (deriv == True):
#         return x * (1 - x)
#     return 1 / (1 + np.exp(-x))
#
# inptest = []
# outtest = []
# for i in range(numtest):
#     xval = random.random()*4 - 2
#     yval = random.random()*4 - 2
#     inptest.append([xval,yval,1])
#     if xval**2+yval**2<1:
#         outtest.append([1])
#     else:
#         outtest.append([0])
# xtest = np.array(inptest)
# ytest = np.array(outtest)
# l0test = xtest
# l1test = nonlin(np.dot(l0test, syn0))
# l2test = nonlin(np.dot(l1test, syn1))
# # print(l2test.tolist())
# # print(ytest.tolist())
# expY = l2test.tolist()
# theY = ytest.tolist()
# wrong = 0
# for k in range(len(expY)):
#     for o in range(len(expY[k])):
#         if (expY[k][o]>.5 and theY[k][o]==0) or (expY[k][o]<.5 and theY[k][o]==1):
#             wrong += 1
# toprint = ""
# toprint += str(wrong)+' wrong out of '+str(numtest)+'\n'
# toprint += str(100*(numtest-wrong)/numtest)+"%"+'\n'
#
# toprint += '\nsyn0: '+str(syn0.tolist())+' \nsyn1: '+str(syn1.tolist())+'\n'
# # toprint += '\nIterations: '+str(it)+' \n\n'
# print(toprint)

# import numpy as np
# inptest = [[0,0,1]]
# outtest = [[1]]
#
syn0array = [[0.8902890389154591, 1.3293843547346973, 19.252004933698547, 27.69359158677681], [19.67463097005881, -17.45319944679977, 0.852502584984745, -2.0879466166387974], [-15.691941244648648, -12.542892473331287, -14.364903298877714, 16.560160134789164]]
syn1array = [[-113.61669849220947], [-111.82420971618576], [-112.28099046233838], [109.99515805207507]]
# syn0 = np.array(syn0array)
# syn1 = np.array(syn1array)
# numtest = 1
# def nonlin(x, deriv=False):
#     if (deriv == True):
#         return x * (1 - x)
#     return 1 / (1 + np.exp(-x))
# xtest = np.array(inptest)
# ytest = np.array(outtest)
# l0test = xtest
# l1test = nonlin(np.dot(l0test, syn0))
# l2test = nonlin(np.dot(l1test, syn1))
# expY = l2test.tolist()
# theY = ytest.tolist()
# print(expY)
# print(theY)


# for i in range(len(syn0array)):
#     toprint = ''
#     for j in range(len(syn0array[0])):
#         toprint += "w-l0["+str(i)+"]l1["+str(j)+"]: "+str(syn0array[i][j]) + '\n'
#     print(toprint)
# # print()
# for i in range(len(syn1array)):
#     toprint = ''
#     for j in range(len(syn1array[0])):
#         toprint += "w-l1["+str(i)+"]l2["+str(j)+"]: "+str(syn1array[i][j])
#     print(toprint)
#     # print()
# print()

# for excel
# for i in range(len(syn0array)):
#     toprint = ''
#     for j in range(len(syn0array[0])):
#         toprint += str(syn0array[i][j]) + '\t'
#     print(toprint)

text = '''in the first part of this series we
00:01
learned about how San Francisco's
00:03
Chinese fought exclusion in this part
00:05
will visit the Mississippi Delta where
00:07
Chinese community has played an
00:09
unexpectedly important role the
00:15
Mississippi Delta home of the blues and
00:18
list fields of green and a land
00:20
cultivated by the hands of slaves but in
00:23
between for more than a hundred years
00:25
the Delta has also been home to small
00:27
but influential Chinese communities it's
00:29
been navigating an identity that's both
00:31
American and Chinese the corn when they
00:40
describe how that when I get that this
00:43
is Sally and Gilroy Chow and this is
00:45
their 46 year old walk we heard about
00:47
these dinner parties they throw to get
00:49
together with friends and eat southern
00:51
style Chinese food like fried rice with
00:53
lots of bacon so we decide to go meet
00:56
them and find out how their families
00:57
ended up in the Delta this is a store
01:00
that I grew up in many many years ago we
01:03
lived in the back of the store every
01:05
store we bought another house like most
01:07
of the Delta Chinese of the time Sally's
01:09
parents opened and ran a grocery store
01:11
the Chinese originally came here to work
01:13
in the cotton fields with the end of
01:15
slavery plantation owners could no
01:17
longer depend on the free labor of
01:18
slaves so they look to the Chinese who
01:20
were cheap disposable and politically
01:22
voiceless
01:23
but with harsh conditions and little pay
01:25
working in the fields didn't last long
01:27
they soon started opening grocery stores
01:30
in small towns up and down the Delta
01:32
Yemeni was a phenomenon when I think
01:36
about how the Chinese came they just
01:41
settled in the Delta from Memphis to
01:44
Vicksburg I mean just look at it it
01:45
really sailed a particular need because
01:50
nobody else wanted to do it
01:52
these stores played a uniquely important
01:55
role in the segregated self serving the
01:57
black community when the white community
01:59
wouldn't and this is significant because
02:01
I met more than 70% of the population
02:03
got their groceries and everyday goods
02:05
from a tiny Chinese community Freitas
02:07
family store a minsang started out in
02:10
the 1930s as two different buildings
02:12
across the street from each other one
02:14
serving black people the other serving
02:16
white people neither black nor white the
02:18
Chinese community found themselves in
02:20
the middle it was like oh the rori lying
02:23
road all that there were the whites and
02:28
the blacks in the chale
02:31
we all stayed in our line and we will
02:35
find until we crossed over the Chinese
02:40
grocers depended on the black community
02:42
for business and also served them in
02:44
very practical ways like when jeans
02:46
father's customers couldn't pay for
02:47
their groceries right away
02:49
he let them use credit people didn't
02:51
have that much cash and so he would have
02:53
created and they would come in one week
02:54
pay a little bit on a bill and take out
02:57
more and that was just kind of how they
03:00
survived this kind of trust was
03:03
essential because of the economic burden
03:04
non-whites face regime grew up the
03:07
median annual income for whites was just
03:09
over $4,000 more than four times the
03:12
median income of non-whites
03:14
over dinner Sally and Gilroy's friends
03:16
had plenty of grocery store memories to
03:18
share with me
03:19
whoa the worse when you were old enough
03:31
to be able to see over the counter many
03:32
of us started working in the store it
03:34
was just expected of us living and
03:38
working alongside our mom and dad was
03:43
seven days a week
03:45
morning until night I mean even
03:48
Christmas done they open 365 days a year
03:54
you know there's one thing I didn't even
03:56
realize during the exclusion act the
03:58
Chinese were not allowed to own property
04:00
so they lived in the back of their
04:02
stores even when exclusion ended in 1943
04:05
many families couldn't afford to buy a
04:07
new home we live behind the grocery
04:09
store one big room divided into two ins
04:13
we didn't know anything else so we
04:15
thought it was kind of fun but you know
04:16
as we went to school and realized people
04:19
had homes we thought was that different
04:22
when it came time for Frieda to go to
04:25
school it was the first year that the
04:26
town she lived in Greenville allowed
04:28
Chinese children to go to white public
04:30
school far today at all the shiny
04:34
children had to attend this one won't go
04:36
heil some of these school houses were
04:38
built by the Southern Baptist Church
04:40
which remained a big part of Delta
04:41
Chinese life before we disaster
04:43
blessings on those food ferreted even
04:47
with their busy lives between the store
04:48
and family the Chinese still found time
04:51
to get together for celebrations dances
04:53
and of course food there was a definite
04:56
camaraderie with the kids in the Delta
05:01
it could be a birthday party or wedding
05:03
where they would have danced we all just
05:08
love getting together and the food is
05:09
always phenomenal here we are we're all
05:13
lonely in the grocery store and there is
05:15
absolutely nothing to look forward to
05:18
and and so you can imagine that I mean
05:22
here here was something a social event
05:26
that the Chinese could could really look
05:30
forward to for many years the community
05:32
thrived in the Delta but over time as
05:35
more farm jobs were lost some machines
05:37
unemployment increased and so did
05:39
poverty and drug use Chinese owned
05:42
grocery stores became easy targets my
05:45
brothers I mean they had been victims of
05:49
two armed robberies within last few
05:53
years luckily they have survived we just
05:57
don't even wanna today most of the
06:05
Chinese grocery stores are closed the
06:07
end of the exclusion act brought new
06:09
work opportunities and the original
06:11
grocers fulfilled their duty of working
06:13
every day of the year to send their kids
06:15
off to college many of their children
06:17
grow up to be pharmacist some served in
06:19
the militaries like Sally's
06:20
there Audrey and Gilmer worked on
06:22
multiple Apollo missions for NASA but
06:24
even though they've been here for so
06:26
long the Delta trainees are still often
06:28
seen as outsiders I had an occasion to
06:31
where I was walking into an office
06:33
building and some dear little lady said
06:36
honey she says are you ornamental and I
06:40
didn't quite know how to answer her I
06:42
said sometimes it happens to me all the
06:46
time you know like how long you been
06:48
here
06:48
or who taught you English because always
06:53
where are we far I mean that's a great
06:58
question I think about that myself all
07:00
the time are we always foreigners
07:01
because of our because of our appearance
07:05
because of our appearance we just look
07:07
like we just got here I mean we don't
07:10
look like American people despite these
07:17
interactions for the Chinese community
07:19
here the Delta will always be home
07:22
Audrey why do you love it as it's so
07:25
peaceful you can't I'll turn my cell
07:27
phone off and so I'll just bitch and
07:29
nobody's calling me it's just solid -
07:33
you enjoying God's creation Sally you're
07:37
a Jean Frieda and audre k-- these
07:39
friends are some of the few Chinese left
07:41
in the Mississippi Delta but they remain
07:44
a close-knit group gathering over food
07:46
to preserve the memory and legacy of
07:48
their families the Chinese American
07:52
people definitely made a contribution in
07:56
the Mississippi Delta they came and they
08:00
definitely made a big contribution here
08:03
they do
08:07
if you liked this episode on the
08:09
mississippi chinese check out the next
08:11
one on saint gabriel valley where new
08:13
immigrants are completely changing the
08:15
restaurant scene even chinese people
08:17
think they have the best Chinese food in
08:19
America

'''
newtext = text.split('\n')
finaltext = ''
for i in range(0,len(newtext),2):
    finaltext += ' ' + newtext[i]
print(finaltext)