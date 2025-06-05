import pysolr
from config import GLOBAL_KEYS, LABEL_LIST

SOLR_INSTANCE = pysolr.Solr("http://localhost:8983/solr/group", always_commit=True, timeout=10)
"""
詳しくはこちら：https://pypi.org/project/pysolr/
・変更内容を明示的に反映させたい場合は、always_commit=FalseとしてSOLR.commit()を呼び出す必要がある
"""

def main():
    data = fetch_data_by_global_key(
        global_keys = GLOBAL_KEYS
    )
    labeled_data = label_data_by_automl(
        data = data
    )
    update_data_in_solr(
        data = labeled_data
    )


# ----- modules -----

def fetch_data_by_global_key(global_keys):
    """
    特定のglobal_keyを持つデータをSolrから取得する
    """
    results = []
    for global_key in global_keys:
        query = f"global_key:{global_key},fl='global_key,images'"
        try:
            response = SOLR_INSTANCE.search(query)
            results.append(response.docs[0])
        except pysolr.SolrError as e:
            print(f"データフェッチ時のエラー({global_key}): {e}")
    return results


def label_data_by_automl(data):
    """
    AutoMLによるラベリングを行う
    """
    return []


def update_data_in_solr(data):
    """
    Solrにデータを更新する
    """
    try:
        SOLR_INSTANCE.add(data)
        print('Solr上のデータを更新しました。')
    except pysolr.SolrError as e:
        print(f"更新時のエラー: {e}")

# ----- エントリーポイント -----

if __name__ == "__main__":
    main()
