import plotly.graph_objects as go


class Charts:

    @staticmethod
    def health_score(score):

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=score,

            title={"text": "Health Score"},

            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 40], "color": "#ffcccc"},
                    {"range": [40, 70], "color": "#fff4b3"},
                    {"range": [70, 100], "color": "#ccffcc"}
                ]
            }

        ))

        return fig

    @staticmethod
    def bar_chart(data):

        fig = go.Figure()

        fig.add_bar(

            x=list(data.keys()),

            y=list(data.values())

        )

        return fig