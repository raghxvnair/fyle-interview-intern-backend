from core.models.assignments import AssignmentStateEnum, GradeEnum

def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]

def test_get_all_teachers(client, h_principal):
    response = client.get(
        '/principal/teachers',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']


def test_grade_assignment_draft_assignment(client, h_principal, h_student_1):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    content = "ABCD TESTPOST"
    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': content
        })

    response = client.post(
        '/principal/assignments/grade',
        headers=h_principal,
        json={
            'id': 6,
            'grade': GradeEnum.A.value
        }
    )

    assert response.status_code == 400

def test_regrade_assignment(client, h_principal, h_student_1, h_teacher_2):

    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 6,
            'teacher_id': 2
        })

    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_2,
        json={
            'id': 6,
            'grade': GradeEnum.B.value
        }
    )

    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 6,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['grade'] == GradeEnum.C.value

# def test_regrade_assignment_if_not_graded(client, h_principal):
#     """
#     Test regrading an assignment if not in graded state.
#     """

#     response = client.post(
#         '/principal/assignments/grade',
#         json={
#             'id': 3,
#             'grade':GradeEnum.A
#         },
#         headers=h_principal
#     )

#     assert response.status_code == 400

# def test_regrade_assignment_wrong_teacher(client, h_principal):
#     """
#     Test regrading an assignment by a principal when the assignment was not submitted to them.
#     """

#     response = client.post(
#         '/principal/assignments/grade',
#         json={
#             'id': 6,
#             'grade': GradeEnum.A.value
#         },
#         headers=h_principal
#     )

#     assert response.status_code == 404

# def test_regrade_assignment_missing_grade(client, h_principal):
#     """
#     Test regrading an assignment without providing the grade.
#     """

#     response = client.post(
#         '/principal/assignments/grade',
#         json={
#             'id': 8
#         },
#         headers=h_principal
#     )

#     assert response.status_code == 400