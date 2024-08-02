class Solution:
    rating = []

    def fromASeq(self, currentSeq, newIndex, typer):
        # print(currentSeq, newIndex, 'inside')
        if len(currentSeq) >= 3 or len(self.rating) <= newIndex:
            if len(currentSeq) == 3 :
                # print(currentSeq, 'reached end')
                self.answer += 1
            return

        if typer == 'increasing':
            if len(currentSeq) == 0 or (len(currentSeq) > 0 and currentSeq[-1] < self.rating[newIndex]):
                currentSeq.append(self.rating[newIndex])
                newIndex += 1
                self.fromASeq(currentSeq, newIndex, 'increasing')
                # print("----", currentSeq)
                if len(currentSeq) > 0:
                    currentSeq.pop()
                    newIndex -= 1

            self.fromASeq(currentSeq, newIndex + 1, 'increasing')

        if typer == 'descreasing':
            if len(currentSeq) == 0 or (len(currentSeq) > 0 and currentSeq[-1] > self.rating[newIndex]):
                currentSeq.append(self.rating[newIndex])
                newIndex += 1
                self.fromASeq(currentSeq, newIndex, 'descreasing')
                # print("----", currentSeq)
                if len(currentSeq) > 0:
                    currentSeq.pop()
                    newIndex -= 1

            self.fromASeq(currentSeq, newIndex + 1, 'descreasing')

    def numTeams(self, rating: List[int]) -> int:

        return 0

        self.rating = rating
        self.answer = 0
        self.fromASeq([], 0, 'increasing')
        self.fromASeq([], 0, 'descreasing')

        return self.answer
