from builtins import str, super


def create_git_object(type, object_data):
    if type == 'users':
        return GitUser(object_data)
    elif type == 'repositories':
        return GitRepo(object_data)


class GitObject:
    def __init__(self, object_data):
        self.id = object_data.get('id')
        self.url = object_data.get('html_url')

    def get(self, property):
        return self.__dict__.get(property)

    def __repr__(self):
        return str(self.__dict__)


class GitUser(GitObject):
    def __init__(self, user_data):
        super(GitUser, self).__init__(user_data)
        self.username = user_data.get('login')

    def __gt__(self, other):
        return self.username > other.username

    def __repr__(self):
        return self.username


class GitRepo(GitObject):
    def __init__(self, repo_data):
        super(GitRepo, self).__init__(repo_data)
        self.name = repo_data.get('name')
        self.fullname = repo_data.get('full_name')
        self.owner = GitUser(repo_data['owner'])

    def __gt__(self, other):
        return self.name > other.name
