from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class KalkulatorApp(App):
    operatory = ("+", "-", "*", "/")
    kropka = False
    zero = False
    bug = False

    def build(self):
        self.icon = "Logo.png"
        self.pudlo = TextInput(
            text=" ",
            multiline=False,
            readonly=True,
            halign="center",
            font_size=50
        )
        okno_glowne = BoxLayout(orientation="vertical")
        okno_glowne.add_widget(self.pudlo)

        przyciski_tytuly = (
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            (".", "0", "C", "+")
        )
        for rzad in przyciski_tytuly:
            okna_przyciskow = BoxLayout(orientation="horizontal")
            for kolumna in rzad:
                przycisk = Button(
                    text=kolumna,
                    size_hint=(1, 1)
                )
                przycisk.bind(on_press=self.akcja_przycisk)
                okna_przyciskow.add_widget(przycisk)
            okno_glowne.add_widget(okna_przyciskow)

        wynik = Button(
            text = "=",
            size_hint=(1, 1)
        )
        wynik.bind(on_press=self.akcja_wynik)
        okno_glowne.add_widget(wynik)

        return okno_glowne

    def akcja_przycisk(self, instance):
        poprzednie = self.pudlo.text[len(self.pudlo.text)-1]
        teraz = instance.text

        if teraz == "C":
            self.kropka = False
            self.zero = False
            self.bug = False
            self.pudlo.text = " "

        elif not self.bug:
            if (teraz in self.operatory or teraz == ".") and poprzednie == " " or \
                    teraz != "." and poprzednie == "0" and len(self.pudlo.text) < 3:
                print(self.kropka)
                return

            elif teraz == "." and (self.kropka or poprzednie in self.operatory):
                return

            elif teraz in self.operatory and poprzednie in self.operatory:

                self.pudlo.text = self.pudlo.text[0:len(self.pudlo.text)-1] + teraz
                self.kropka = False
                print(self.kropka)

            else:
                if teraz == ".":
                    self.kropka = True
                    self.zero = False
                    self.pudlo.text += teraz
                elif teraz == "0" and poprzednie in self.operatory:
                    self.zero = True
                    self.kropka = False
                    self.pudlo.text += teraz
                elif teraz in self.operatory and poprzednie == ".":
                    return
                else:
                    self.pudlo.text += teraz

    def akcja_wynik(self, instance):

        if not self.bug:
            try:
                self.pudlo.text = str(eval(self.pudlo.text))
                self.bug = True

            except ZeroDivisionError:
                self.pudlo.text = "Nie można dzielić przez zero."
                self.bug = True


if __name__ == "__main__":
    moja_apka = KalkulatorApp()
    moja_apka.run()
