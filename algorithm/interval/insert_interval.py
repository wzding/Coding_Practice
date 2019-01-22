# https://www.lintcode.com/problem/insert-interval/description
class Solution:
      # @param intervals: Sorted interval list.
      # @param newInterval: new interval.
      # @return: A new interval list.
      def insert(self, intervals, new_interval):
          answer = []

          index = 0
          while index < len(intervals) and intervals[index].start < new_interval.start:
              index += 1
              intervals.insert(index, new_interval)

          last = None
          for item in intervals:
              if last == None or last.end < item.start:
                  answer.append(item)
                  last = item
              else:
                  last.end = max(last.end, item.end)
          return answer
