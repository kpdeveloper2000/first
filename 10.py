from nltk.corpus import stopwords
# import nltk
# nltk.download('stopwords')
stop_words = stopwords.words('english')


def remove_numbers(text):
    list = []
    for i in text:
        if not i.isdigit():
            list.append(i.lower())
    return list


def word_count(word_list):
    unique_words, total = {}, 0
    for list in word_list:
        for word in list:
            if word not in unique_words:
                unique_words[word] = 1
            elif word in unique_words:
                val = unique_words[word] + 1
                unique_words[word] = val
            total = total + 1
    return unique_words, total


prob_SPAM, prob_NOTspam = 0.0110, 0.9890
words_for_notspam = []
words_for_spam = []

file = open("SMSSpamCollection.txt", "r")
text = file.read()
file.close()
textlines = text.splitlines()

for sent in textlines:
    if sent[:4] == "spam":
        tok_words = sent.split()
        line = [word for word in tok_words if word not in stop_words]
        words_for_spam.append(remove_numbers(line))
    elif sent[:3] == "ham":
        tok_words = sent.split()
        line = [word for word in tok_words if word not in stop_words]
        words_for_notspam.append(remove_numbers(line))

prob_notspam = {}
prob_spam = {}
u_w_notspam, n_w_notspam = word_count(words_for_notspam)
u_w_spam, n_w_spam = word_count(words_for_spam)

for item in u_w_notspam:
    prob_notspam[item] = u_w_notspam[item] / n_w_notspam
for item in u_w_spam:
    prob_spam[item] = u_w_spam[item] / n_w_spam
for item in u_w_notspam:
    if item not in u_w_spam:
        prob_spam[item] = 0.001
for item in u_w_spam:
    if item not in u_w_notspam:
        prob_notspam[item] = 0.001

data = input("Enter the sentences: ")
tok_words = data.split()
xnew = [word for word in tok_words if word not in stop_words]
xnew = remove_numbers(xnew)

# calculation for case of notspam
up = 1 * prob_NOTspam
for i in xnew:
    if i in prob_notspam:
        up = up * prob_notspam[i]
down = 1
for i in xnew:
    if i in prob_notspam:
        down = down * prob_spam[i]
p_notspam_xnew = up / (up + down)

# calculation for case of spam
up = 1 * prob_SPAM
for i in xnew:
    if i in prob_spam:
        up = up * prob_spam[i]
down = 1
for i in xnew:
    if i in prob_spam:
        down = down * prob_notspam[i]
p_spam_xnew = up / (up + down)

# message to user
if p_spam_xnew > p_notspam_xnew:
    print("The message is spam.")
else:
    print("The message is not spam.")
