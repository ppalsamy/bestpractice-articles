For Java Application
1. Gradle version is 5.0 or above.
2. Add the renovate.json file in to your repository default branch.
   Example: renovate.json
 ~~~
   {
    "$schema": "https://docs.renovatebot.com/renovate-schema.json"
  }
~~~
For JS Application
Add the renovate.json file into your repository default branch.
Example renovate.json
~~~
{
    "$schema": "https://docs.renovatebot.com/renovate-schema.json"
}
~~~
It is highly recommended that you run the Renovate bot on a separate branch. See the example below for guidance on changing the base branch:
~~~
{
    "$schema": "https://docs.renovatebot.com/renovate-schema.json",
    "baseBranches": ["develop"]
}
~~~
