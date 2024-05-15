from packets.samitler import Samitleri_al
if __name__ == "__main__":
    cumle =str(input("cumleni daxil edin: "))
    samitler_list = Samitleri_al(cumle)
    print(f"Cumledeki samit herfler: {samitler_list}" )