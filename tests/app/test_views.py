import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Pet_list_view(client):
    instance1 = test_helpers.create_app_Pet()
    instance2 = test_helpers.create_app_Pet()
    url = reverse("app_Pet_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Pet_create_view(client):
    url = reverse("app_Pet_create")
    data = {
        "title": "text",
        "description": "text",
        "image": "anImage",
        "price": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Pet_detail_view(client):
    instance = test_helpers.create_app_Pet()
    url = reverse("app_Pet_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Pet_update_view(client):
    instance = test_helpers.create_app_Pet()
    url = reverse("app_Pet_update", args=[instance.pk, ])
    data = {
        "title": "text",
        "description": "text",
        "image": "anImage",
        "price": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Service_list_view(client):
    instance1 = test_helpers.create_app_Service()
    instance2 = test_helpers.create_app_Service()
    url = reverse("app_Service_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Service_create_view(client):
    url = reverse("app_Service_create")
    data = {
        "description": "text",
        "imege": "anImage",
        "service_title": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Service_detail_view(client):
    instance = test_helpers.create_app_Service()
    url = reverse("app_Service_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Service_update_view(client):
    instance = test_helpers.create_app_Service()
    url = reverse("app_Service_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "imege": "anImage",
        "service_title": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Our_team_list_view(client):
    instance1 = test_helpers.create_app_Our_team()
    instance2 = test_helpers.create_app_Our_team()
    url = reverse("app_Our_team_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Our_team_create_view(client):
    url = reverse("app_Our_team_create")
    data = {
        "full_name": "text",
        "image": "anImage",
        "age": 1,
        "information": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Our_team_detail_view(client):
    instance = test_helpers.create_app_Our_team()
    url = reverse("app_Our_team_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Our_team_update_view(client):
    instance = test_helpers.create_app_Our_team()
    url = reverse("app_Our_team_update", args=[instance.pk, ])
    data = {
        "full_name": "text",
        "image": "anImage",
        "age": 1,
        "information": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
