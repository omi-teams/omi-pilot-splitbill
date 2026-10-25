# split-bill — Đặc tả sản phẩm v1

## Người dùng
PO và bạn bè, dùng trên terminal (Windows, macOS, Linux).

## Vấn đề
Chia tiền hoá đơn đi ăn bằng tay dễ sai khi có tip và làm tròn.

## Tính năng v1
1. **Chia đều:** `split-bill 450000 --people 4` → mỗi người 112500.
2. **Tip theo %:** `--tip 10` cộng 10% vào tổng trước khi chia. Tiền tip = `tổng × tip / 100`, làm tròn đến đồng (0,5 làm tròn lên).
3. **Làm tròn:** `--round 1000` làm tròn số tiền mỗi người **lên** bội số 1000, rồi in thêm dòng `Dư` (= tổng mọi người trả − tổng hoá đơn sau tip).
4. **Chia theo phần:** `--shares An=2,Binh=1,Chi=1` chia theo tỉ lệ, dùng thay cho `--people`.

### Quy tắc tính
- Tiền là số nguyên VND.
- Khi chia không hết, phần lẻ (đơn vị đồng) được cộng thêm 1đ cho từng người, ưu tiên người có phần thập phân lớn nhất; nếu bằng nhau thì theo thứ tự nhập. Nhờ vậy tổng luôn khớp đúng hoá đơn. Ví dụ: `100000 --people 3` → `33334, 33333, 33333`.
- Kết quả in ra dạng bảng text đơn giản: mỗi người một dòng (tên, số tiền), dòng cuối là `Tổng`. Với `--people`, tên là `Người 1..N`. Khi dùng `--round`, có thêm dòng `Dư` ngay dưới dòng `Tổng`.

### Lỗi
Lỗi được in ra stderr với thông báo rõ ràng, mã thoát 2, trong các trường hợp:
- số tiền ≤ 0 hoặc không phải số nguyên;
- `--people` < 1;
- tip âm;
- `--round` ≤ 0;
- `--shares` rỗng, sai cú pháp, có phần ≤ 0 hoặc tên trùng;
- dùng cả `--people` và `--shares` cùng lúc, hoặc không dùng cái nào.

## Ngoài phạm vi
Nhiều loại tiền tệ, số tiền lẻ (chỉ VND số nguyên), lưu lịch sử, nhiều hoá đơn, giao diện web, phát hành lên PyPI, deploy.

## Ràng buộc
- Python 3.11+, chỉ dùng stdlib, test bằng `unittest`.
- CI dùng GitHub Actions bản miễn phí. Không tốn thêm chi phí.

## Stack
| Lựa chọn | Lý do |
|---|---|
| Python 3.11+ | PO yêu cầu, chạy được trên cả 3 hệ điều hành. |
| `argparse` | Có sẵn trong stdlib, đủ cho 4 tuỳ chọn. |
| `unittest` | Có sẵn trong stdlib, không thêm dependency. |
| `pyproject.toml` + setuptools, entry point `split-bill` | Cài được bằng `pip install git+https://github.com/omi-teams/omi-pilot-splitbill@staging`, chưa cần PyPI. |
| GitHub Actions (ma trận Ubuntu/Windows/macOS, Python 3.11) | Miễn phí, kiểm tra được cả 3 hệ điều hành. |

## Tiêu chí thành công
- 4 tính năng chạy đúng theo các ví dụ ở trên, đều có unittest và CI xanh.
- PO cài được bằng `pip install git+https://github.com/omi-teams/omi-pilot-splitbill@staging` và chạy thử `split-bill` thành công.
