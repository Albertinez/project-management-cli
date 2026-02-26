from models.project import Project

def test_project_creation():
    project = Project("CLI Tool", "Build CLI", "2026-12-31")
    assert project.title == "CLI Tool"
    assert project.tasks == []