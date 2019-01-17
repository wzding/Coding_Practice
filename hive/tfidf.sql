/*
lateral view
https://stackoverflow.com/questions/36876959/sparksql-can-i-explode-two-different-variables-in-the-same-query
explode
https://cwiki.apache.org/confluence/display/Hive/LanguageManual+LateralView
tfidf hive
https://hivemall.incubator.apache.org/userguide/ft_engineering/tfidf.html
*/

-- corpus contain pageid and text
create or replace view corpus_exploded as
  select pageid, word
  from
  corpus lateral view explode(tokenize(text, true)) t as word
  where not is_stopword(word);

create or replace view tf as
  select pageid, word, freq from
  (select pageid, tf(word) as word2freq
  from corpus_exploded
  group by pageid
  ) t1
  lateral view explode(word2freq) t2 as word, freq;

create or replace view df as
  select word, count(distinct pageid) ndoc
  from corpus_exploded
  group by word;

select count(distinct pageid) from corpus;
set hivevar:n_docs = 1000000;

create or replace view tfidf as
select tf.pageid, tf.word,
tf.freq * (log(10, cast(${n_docs} as float) / df.ndoc)) as tfidf
from tf
join df
on tf.word = df.word
order by tfidf desc;
