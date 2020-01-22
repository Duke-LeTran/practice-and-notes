# If and Only If

. | Symbol | Type_if | Sufficient vs Necessary | English
:---:  | :---:  | :---:  | :---:  | :--- 
1 | A ← B | If | B is sufficient for A | If the fruit is an apple, that is sufficient for Madison to eat (tho she’ll eat other fruits too)
2 | A → B | Only If | B is necessary for A | Only if the fruit is an apple, a necessary condition, i.e., can’t be other fruits, will then Madison eat it (tho she may also refuse to eat it)
3 | A⟺B | If and only if | B is sufficient and necessary for A | Madison will eat all and only those fruits that are apples. She will not leave any apple uneaten, and she will not eat any other type of fruit.


## Variables
* B | fruit is an apple
* A | Madison eats the apple

# Truth Table
.    | .    | B sufficient    | B is necessary    | Sufficient & Necessary 
:---:  | :---:  | :---:  | :---:  | :---: 
.    | .    | if   | only if   | iff 
A    | B    | A←B | A→B | A⟺B
T    | T    | T    | T    | T 
T    | *F*  | *F*  | T    | *F* 
*F*  | T    | T    | *F*  | *F* 
*F*  | F    | T    | T    | T 


# Filter on join or where clause

## Summary
* NOTE, it is important -- inner join would make tese differences the same. Only in OUTER join does this matter
* JOIN:  Filtering in the JOIN allows the possibility of no matches (effectively does nothing)
* WHERE: Filtering in the WHERE clause may discard some hospital accounts.

## Two events
* B | Match
* A | Filter

## if statements
* JOIN: **Only if** a match happens (necessary condition), will filtering occur (tho nulls may also be returned) 
* WHERE: **If and only if** a match happens, will filtering definitely occur (non matches are discarded, lose hospital accounts)

. | Symbol | Type_if | Sufficient vs Necessary | English
:---:  | :---:  | :---:  | :---:  | :--- 
2 | A → B | Only If | B is necessary for A | Only if the match happens, a necessary condition, i.e., can’t be other matches, will then the filter happen (tho we could  return nulls tho)
3 | A⟺B | If and only if | B is sufficient and necessary for A | Filltering will definitely happen and only by that match condition. She will not leave any apple uneaten, and she will not eat any other type of fruit.



```{SQL}
-- ##JOIN CLAUSE, note that all nulls on left are included, a (ONLY IF) dx
USE Clarity_Aug19
SELECT a.HSP_ACCOUNT_NAME "Patient Name",
       a.HSP_ACCOUNT_ID "a_HAR",
       dx.HSP_ACCOUNT_ID "dx_HAR",
       dx.DX_ID "Diagnosis ID",
       dx.FINAL_DX_POA_C "POA?"
  FROM HSP_ACCOUNT a LEFT OUTER JOIN HSP_ACCT_DX_LIST dx
      ON a.HSP_ACCOUNT_ID = dx.HSP_ACCOUNT_ID
--      AND dx.FINAL_DX_POA_C IS NOT NULL
ORDER BY a_HAR
--WHERE dx.FINAL_DX_POA_C = 1

-- ## JOIN CLAUSE, tbl switched, dx (ONLY IF) a
USE Clarity_Aug19
SELECT a.HSP_ACCOUNT_NAME "Patient Name",
       a.HSP_ACCOUNT_ID "a_HAR",
       dx.HSP_ACCOUNT_ID "dx_HAR",
       dx.DX_ID "Diagnosis ID",
       dx.FINAL_DX_POA_C "POA?"
  FROM HSP_ACCT_DX_LIST dx LEFT OUTER JOIN HSP_ACCOUNT a
      ON a.HSP_ACCOUNT_ID = dx.HSP_ACCOUNT_ID
      AND dx.FINAL_DX_POA_C = 1
ORDER BY a_HAR
--WHERE dx.FINAL_DX_POA_C <> 1 AND dx.FINAL_DX_POA_C IS NOT NULL

-- ##WHERE CLAUSE, effectively an inner join, if and only if (IFF)
USE Clarity_Aug19
SELECT a.HSP_ACCOUNT_NAME "Patient Name",
       a.HSP_ACCOUNT_ID "a_HAR",
       dx.HSP_ACCOUNT_ID "dx_HAR",
       dx.DX_ID "Diagnosis ID",
       dx.FINAL_DX_POA_C "POA?"
  FROM HSP_ACCOUNT a LEFT OUTER JOIN HSP_ACCT_DX_LIST dx
      ON a.HSP_ACCOUNT_ID = dx.HSP_ACCOUNT_ID
--      AND dx.FINAL_DX_POA_C IS NOT NULL
ORDER BY a_HAR
--WHERE dx.FINAL_DX_POA_C = 1


SELECT dx.FINAL_DX_POA_C, COUNT(*) count FROM HSP_ACCT_DX_LIST dx
GROUP BY dx.FINAL_DX_POA_C
```

![ifandonlyifSQL](https://github.com/Duke-LeTran/practice-and-notes/blob/master/pics/2020-01-22%20ifnonlyif_SQL.png)

# Links
* https://math.stackexchange.com/questions/68293/what-is-the-difference-between-only-if-and-iff
* https://stackoverflow.com/questions/354070/sql-join-where-clause-vs-on-clause