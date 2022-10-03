from mrjob.job import MRJob

class MRRatingCounter(MRJob):
    def mapper(self, key, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield rating, 1

    def reducer(self, rating, occurences):
        yield rating, sum(occurences)

if __name__ == '__main__':
    MRRatingCounter.run()
    

## TO RUN: type "!python RatingCounter.py ml-100k/u.data" in console
    ## make sure ratingcounter and ml-100k are in Users>taterosen for it to work
