#!/usr/bin/env python3
"""X10-019: minimal offline Flutter starter (template, not a certified Golden).

Only writes to a new empty directory. Never invokes Flutter, edits a consumer,
installs packages, accesses GitHub, or claims a device/build result.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

NAME = re.compile(r"^[a-z][a-z0-9_]{2,48}$")

FILES = {
    "pubspec.yaml": """name: __APP_NAME__
description: Minimal App Factory starter; adapt with an approved Product Bible.
publish_to: none
version: 0.1.0+1
environment:
  sdk: '>=3.5.0 <4.0.0'
dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
dev_dependencies:
  flutter_test:
    sdk: flutter
flutter:
  uses-material-design: true
  generate: true
""",
    "l10n.yaml": """arb-dir: lib/l10n
template-arb-file: app_en.arb
output-localization-file: app_localizations.dart
output-dir: lib/l10n/generated
synthetic-package: false
nullable-getter: false
""",
    "lib/l10n/app_en.arb": """{
  "@@locale": "en",
  "homeTitle": "Welcome to your app",
  "continueLabel": "Continue",
  "welcomeMessage": "Your next step starts here"
}
""",
    "lib/l10n/app_it.arb": """{
  "@@locale": "it",
  "homeTitle": "Benvenuto nella tua app",
  "continueLabel": "Continua",
  "welcomeMessage": "Il prossimo passo inizia qui"
}
""",
    "lib/src/theme/app_tokens.dart": """import 'package:flutter/material.dart';

abstract final class AppTokens {
  static const Color seed = Color(0xFF7867B1);
  static const double cornerRadius = 18;
  static const double spacing = 16;

  static ThemeData theme(Brightness brightness) {
    final scheme = ColorScheme.fromSeed(
      seedColor: seed,
      brightness: brightness,
    );
    return ThemeData(
      colorScheme: scheme,
      useMaterial3: true,
      scaffoldBackgroundColor: scheme.surface,
      cardTheme: CardThemeData(
        color: scheme.surfaceContainerLow,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(cornerRadius),
        ),
      ),
    );
  }
}
""",
    "lib/main.dart": """import 'package:flutter/material.dart';
import 'l10n/generated/app_localizations.dart';
import 'src/theme/app_tokens.dart';

void main() => runApp(const StarterApp());

class StarterApp extends StatelessWidget {
  const StarterApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      onGenerateTitle: (context) => AppLocalizations.of(context).homeTitle,
      theme: AppTokens.theme(Brightness.light),
      darkTheme: AppTokens.theme(Brightness.dark),
      themeMode: ThemeMode.system,
      localizationsDelegates: AppLocalizations.localizationsDelegates,
      supportedLocales: AppLocalizations.supportedLocales,
      home: const StarterHome(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class StarterHome extends StatelessWidget {
  const StarterHome({super.key});

  @override
  Widget build(BuildContext context) {
    final texts = AppLocalizations.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(texts.homeTitle)),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(AppTokens.spacing),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text(texts.welcomeMessage,
                style: Theme.of(context).textTheme.headlineSmall),
              const SizedBox(height: AppTokens.spacing),
              FilledButton(
                onPressed: () {},
                child: Text(texts.continueLabel),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
""",
    "test/widget_test.dart": """import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:__APP_NAME__/main.dart';

void main() {
  testWidgets('starter renders in English', (tester) async {
    await tester.pumpWidget(
      const MaterialApp(
        home: StarterApp(),
      ),
    );
    await tester.pumpAndSettle();
    expect(find.text('Welcome to your app'), findsOneWidget);
    expect(find.byType(FilledButton), findsOneWidget);
  });
}
""",
    "README.md": """# __APP_NAME__ — App Factory Flutter starter

Source: App Factory 10x X10-019. This is a scaffold, not a published Golden,
tested app, release APK or automatic Product Bible approval.

Requirements: Flutter SDK supporting Dart >=3.5.0, Android/iOS/Web toolchains
when targeting those platforms. Toolchain versions must be pinned per consumer.

This template only generates Flutter/Dart source. In its directory create the
native platform scaffolds with your installed Flutter CLI (do not overwrite the
generated source), then run:

    flutter pub get
    flutter gen-l10n
    flutter analyze
    flutter test
    flutter build web --release

Before product integration: write Product Bible, customize colors/typography,
choose package identity, translations, licenses and native permission policies.
No login, payment, ads, cloud or AI is enabled by default.
""",
}


def bootstrap(name: str, destination: Path) -> list[Path]:
    if not isinstance(name, str) or not NAME.fullmatch(name):
        raise ValueError("Unsafe Flutter project name")
    if not isinstance(destination, Path) or destination.is_symlink():
        raise ValueError("Destination must be a non-symlink path")
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise FileExistsError("Refusing to overwrite any existing project content")
    # Resolve the root once; all output names are hardcoded paths, never user input.
    root = destination.resolve()
    root.mkdir(parents=True, exist_ok=True)
    paths = []
    for relative, template in FILES.items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(template.replace("__APP_NAME__", name), encoding="utf-8")
        paths.append(target)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    paths = bootstrap(args.name, args.output)
    print("FLUTTER_STARTER_SOURCE_GENERATED " + str(len(paths)))


if __name__ == "__main__":
    main()
