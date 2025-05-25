class VarduSpelesKlase:
    def _init_(self, pareizie_vardi, burti):
        self.pareizie_vardi = pareizie_vardi
        self.minetie_vardi = []
        self.burti = burti

    def ir_veidots_no_burtiem(self, vards):
        temp_burti = self.burti.copy()
        for burts in vards:
            if burts in temp_burti:
                temp_burti.remove(burts)
            else:
                return False
        return True

    def minet_vardu(self, vards):
        if (
            vards in self.pareizie_vardi
            and vards not in self.minetie_vardi
            and self.ir_veidots_no_burtiem(list(vards))
        ):
            self.minetie_vardi.append(vards)
            return True
        return False

    def iegut_statistiku(self):
        return len(self.minetie_vardi), len(self.pareizie_vardi)

    def ir_visi_atmineti(self):
        return set(self.pareizie_vardi) == set(self.minetie_vardi)
