import io

import pandas as pd


class VisualizationRepository:
    def create_prediction_visualization(self, predictions):
        # Create dataframe
        df = pd.DataFrame(predictions)

        # Convert columns
        df["created_on"] = pd.to_datetime(df["created_on"]).dt.date

        # Create table
        pt = pd.pivot_table(
            df[["id", "output", "created_on"]],
            values="id",
            index="created_on",
            columns="output",
            aggfunc="count",
        )

        # Create plot
        plt = pt.plot(
            kind="bar",
            title="Prediction Outcomes per Day",
            xlabel="Date",
            ylabel="Count",
        )

        # Create figure
        fig = plt.get_figure()
        fig.autofmt_xdate()

        # Generate figure
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")

        return buffer.getvalue()
