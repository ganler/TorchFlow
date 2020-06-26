from .mysql import mysql_connector
import matplotlib.pyplot as plt

def viz_model_records():
    plt.figure(figsize=(8, 8))
    p1 = plt.subplot(211)

    recs = mysql_connector().glob_all_records()

    viz_names = []
    viz_model_size = []
    viz_model_loss = []
    x = range(len(recs))

    for rec in recs:
        viz_names.append(f'{rec.model_name}-{rec.record_id}')
        viz_model_size.append(rec.model_size)
    plt.bar(x, viz_model_size, tick_label=viz_names, ec='r', ls='--', lw=2)
    p1.set_ylabel('Model Size')
    p1.set_title('Model Size Distribution')
    for a, b in zip(x, viz_model_size):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

    p2 = plt.subplot(212)
    for rec in recs:
        viz_model_loss.append(rec.record_loss)
    plt.bar(x, viz_model_loss, tick_label=viz_names, ec='r', ls='--', lw=2)
    p2.set_ylabel('Model Loss')
    p2.set_title('Model Loss Distribution')
    for a, b in zip(x, viz_model_loss):
        plt.text(a, b, '%.5f' % b, ha='center', va='bottom', fontsize=10)

    plt.show()