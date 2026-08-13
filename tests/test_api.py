from .conftest import client


def test_create_patient():
    response = client.post(
        "/patients",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "9876543210"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"


def test_get_all_patients():
    response = client.get("/patients")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_patient_by_id():
    response = client.get("/patients/1")

    assert response.status_code == 200


def test_patient_not_found():
    response = client.get("/patients/9999")

    assert response.status_code == 404


def test_create_doctor():
    response = client.post(
        "/doctors",
        json={
            "name": "Dr. Smith",
            "specialization": "Cardiology"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Dr. Smith"


def test_get_all_doctors():
    response = client.get("/doctors")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_doctor_by_id():
    response = client.get("/doctors/1")

    assert response.status_code == 200


def test_doctor_not_found():
    response = client.get("/doctors/9999")

    assert response.status_code == 404


def test_create_appointment():
    response = client.post(
        "/appointments",
        json={
            "patient_id": 1,
            "doctor_id": 1,
            "appointment_start": "2026-08-13T10:00:00",
            "appointment_end": "2026-08-13T11:00:00"
        }
    )

    assert response.status_code == 201


def test_get_all_appointments():
    response = client.get("/appointments")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_appointment_by_id():
    response = client.get("/appointments/1")

    assert response.status_code == 200


def test_appointment_not_found():
    response = client.get("/appointments/9999")

    assert response.status_code == 404


def test_overlapping_appointment():
    response = client.post(
        "/appointments",
        json={
            "patient_id": 1,
            "doctor_id": 1,
            "appointment_start": "2026-08-13T10:30:00",
            "appointment_end": "2026-08-13T11:30:00"
        }
    )

    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == "Appointment overlaps with existing appointment"
    )