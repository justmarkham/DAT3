#!/usr/bin/env python

from __future__ import division
from collections import Counter

# load data and keep around in convenient forms
with open('/Users/sinanozdemir/Dropbox/Code/user_brand.csv') as f:
  data = [line.strip().split(",") for line in f]
brandsfor = dict()
for user, brand in data:
  brandsfor.setdefault(user, set()).add(brand)
# count frequencies that brands appear, for normalizing by
frequency = Counter([line[1] for line in data])

def jaccard(firsts, seconds):
  """
  This is a sort of weighted Jaccard Index,
  and depends dangerously on the global `frequency`.
  """
  return (sum([1 / frequency.get(brand, 100) for brand in firsts & seconds])/
          sum([1 / frequency.get(brand, 100) for brand in firsts | seconds]))

def safe_brands(brands):
  """
  For convenience, to allow non-set arguments,
  strings and lists are changed to sets.
  """
  if isinstance(brands, str):
    brands = set([brands])
  if isinstance(brands, list):
    brands = set(brands)
  return brands

def recommend_for_brands(brands):
  """
  Return top five recommended brands
  when given brands to recommend for.
  """
  brands = safe_brands(brands)
  bydiff = sorted(brandsfor.items(),
                  key=lambda x: jaccard(brands, x[1]))
  counter = Counter()
  while sum(counter.values()) < 5 or len(counter) < 5:
    for brand in bydiff.pop()[1] - brands:
      counter[brand] += 1 / frequency[brand]
  return [x[0] for x in counter.most_common(5)]

def recommend_for_user(user):
  """
  Get a user's brands and recommend based on them.
  """
  return recommend_for_brands(brandsfor.get(user, set()))

def for_brands(brands):
  """
  Return a pretty-print string of recommendations for brands alone.
  """
  brands = safe_brands(brands)
  recs = recommend_for_brands(brands)
  return "For a user who likes {liked}, we recommend {recs}.".format(
           liked=", ".join(brands),
           recs=", ".join(recs))

def for_user(user):
  """
  Return a pretty-print string of recommendations for a user.
  """
  recs = recommend_for_user(user)
  return "For user {user}, who likes {liked}, we recommend {recs}.".format(
           user=user,
           liked=", ".join(brandsfor.get(user, ["nothing"])),
           recs=", ".join(recs))

if __name__ == "__main__":
  print "\n" + for_brands("Target") + "\n"
  print for_brands("Banana Republic") + "\n"
  print for_user("86184") + "\n"
  print for_user("83126") + "\n"
  