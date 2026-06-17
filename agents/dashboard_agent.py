from jinja2 import Environment, FileSystemLoader

class DashboardAgent:

    def generate(self, results_df, elite_df, output_file):

        env = Environment(loader=FileSystemLoader("templates"))

        template = env.get_template("dashboard.html")

        summary = {
            "total": len(results_df),
            "strong_buy": len(results_df[results_df["Decision"] == "STRONG BUY"]),
            "buy": len(results_df[results_df["Decision"] == "BUY"])
        }

        print(results_df.head())
        
        html = template.render(
                    top_stocks = results_df.head(20).to_dict(orient="records"),
                    elite = elite_df.to_dict(orient="records"),
                    summary = summary
                )

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html)