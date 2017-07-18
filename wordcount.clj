(ns sentences
  (:use     [streamparse.specs])
  (:gen-class))

(defn sentences [options]
   [
    ;; spout configuration
    {"sentences-spout" (python-spout-spec
          options
          "spouts.sentences.Sentences"
          ["sentence"]
          )
    }
    ;; bolt configuration 1
    {"ParseTweet-bolt" (python-bolt-spec
          options
          {"sentences-spout" :shuffle}
          "bolts.parse.ParseTweet"
          ["validwords"]
          )
    }
    ;; bolt configuration 2
    {"TweetCounter-bolt" (python-bolt-spec
          options
          {"sentences-spout" :shuffle}
          "bolts.tweetcounter.TweetCounter"
          ["word" "counts"]
          :p 2
          )
    }
  ]
)
