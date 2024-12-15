from hendler_csv.work_csv_file import show_orders


def refactor_json(data):
    pass


# def show_zoom(work_day):
#     description_for_show_work_day = (
#         f"🗓 Заказ:"
#         f" {(work_day['order'])}\n\n✅Комплектация : "
#         f"{work_day['equipment']}\n\n✅ {work_day['comment']}\n\n"
#         f"✅ {work_day['comment|foto']}")
#     return description_for_show_work_day

def show_zoom(work_day):
    description_for_show_work_day = (
        f""
        f"✅❌{(work_day['order'])}\n\n"
        f"{work_day['equipment']}\n\n{work_day['comment']}\n\n"
        f"{work_day['comment|foto']}")
    return description_for_show_work_day