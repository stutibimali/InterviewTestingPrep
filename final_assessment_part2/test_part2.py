from fastapi.testclient import TestClient

from final_assessment_part2.challenge_api import app
from final_assessment_part2.challenge_core import apply_patch, page_items, total_lines


def test_one_based_pagination_returns_the_requested_page():
    assert page_items(["a", "b", "c", "d"], page=1, size=2) == ["a", "b"]
    assert page_items(["a", "b", "c", "d"], page=2, size=2) == ["c", "d"]


def test_patch_preserves_explicit_false_values():
    assert apply_patch({"active": True, "label": "old"}, {"active": False}) == {
        "active": False,
        "label": "old",
    }


def test_line_total_multiplies_quantity_by_unit_price():
    assert total_lines([{"quantity": 2, "unit_price": 4.5}]) == 9.0


def test_invoice_rejects_a_mismatched_declared_total():
    response = TestClient(app).post(
        "/invoices",
        json={
            "invoice_id": "inv-1",
            "lines": [{"quantity": 2, "unit_price": 4.5}],
            "declared_total": 8,
        },
    )

    assert response.status_code == 422


def test_invoice_creation_returns_created_status():
    response = TestClient(app).post(
        "/invoices",
        json={
            "invoice_id": "inv-1",
            "lines": [{"quantity": 2, "unit_price": 4.5}],
            "declared_total": 9,
        },
    )

    assert response.status_code == 201


def test_invoice_delete_requires_admin_role():
    response = TestClient(app).delete(
        "/invoices/inv-1", headers={"X-Role": "reader"}
    )

    assert response.status_code == 403


def test_missing_invoice_returns_not_found_for_admin():
    response = TestClient(app).delete(
        "/invoices/missing", headers={"X-Role": "admin"}
    )

    assert response.status_code == 404