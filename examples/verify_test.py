from masterqa import MasterQA


class MasterQATests(MasterQA):

    def test_xkcd(self):
        self.open("http://xkcd.com/1512/")
        self.click('a[rel="next"]')
        self.verify()
        self.open("http://xkcd.com/1520/")
        for i in range(2):
            self.click('a[rel="next"]')
        self.verify("Can you find the moon?")
        self.click('a[rel="next"]')
        self.verify("Do the drones look safe?")
        self.click_link_text('Blag')
        self.update_text("input#s", "Robots!\n")
        self.verify("Does it say 'Hooray robots' on the page?")
        self.open("http://xkcd.com/213/")
        for i in range(5):
            self.click('a[rel="prev"]')
        self.verify("Does the page say 'Abnormal Expressions'?")
