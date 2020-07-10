# 2.7.3. Special parameters

By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

A function definition may look like:
```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```
where / and * are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.

# Topics

- 2.7.3.1. [Positional-or-Keyword Arguments](https://github.com/trioXech/python-core/blob/master/2.MoreControlFlowTools/2.7.MoreOnDefiningFunctions/2.7.3.SpecialParameters/2.7.3.1.PositionalOrKeywordArguments)
- 2.7.3.2. [Positional-Only Parameters](https://github.com/trioXech/python-core/blob/master/2.MoreControlFlowTools/2.7.MoreOnDefiningFunctions/2.7.3.SpecialParameters/2.7.3.2.PositionalOnlyParameters)
- 2.7.3.3. [Keyword-Only Arguments](https://github.com/trioXech/python-core/blob/master/2.MoreControlFlowTools/2.7.MoreOnDefiningFunctions/2.7.3.SpecialParameters/2.7.3.3.KeywordOnlyArguments)
- 2.7.3.4. [Function Examples](https://github.com/trioXech/python-core/blob/master/2.MoreControlFlowTools/2.7.MoreOnDefiningFunctions/2.7.3.SpecialParameters/2.7.3.4.FunctionExamples)
- 2.7.3.5. [Recap](https://github.com/trioXech/python-core/blob/master/2.MoreControlFlowTools/2.7.MoreOnDefiningFunctions/2.7.3.SpecialParameters/2.7.3.5.Recap)
