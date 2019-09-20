from github import Github
g = Github("132360a81fcc12d6941efed1fc8c793a5ae14dfe")
for repo in g.get_user().get_repos():
    print(repo.name)
    #
    # to see all the available attributes and methodsrepo.edit(has_wiki=False)
